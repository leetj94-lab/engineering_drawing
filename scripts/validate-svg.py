"""Parse the generated SVG/XML bytes; validate actual title fields and objects."""
import json
import pathlib
import xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'drawings/manifest.json').read_text())
assets={a['id'] for a in manifest['assets']}
standards=manifest['standards']
parsed={}
for d in manifest['drawings']:
    root=ET.parse(ROOT/'drawings'/d['file']).getroot()
    assert root.tag=='{http://www.w3.org/2000/svg}svg'
    assert not any(n.tag.endswith('script') or any(k.lower().startswith('on') for k in n.attrib) for n in root.iter())
    fields={n.attrib['data-title-field']:''.join(n.itertext()).strip() for n in root.iter() if 'data-title-field' in n.attrib}
    objects=[dict(n.attrib) for n in root.iter() if 'data-object-id' in n.attrib]
    assert len(objects)==len(d['objects'])
    assert len({o['data-object-id'] for o in objects})==len(objects)
    for obj in objects:
        declared=json.loads(obj['data-signature'])
        assert obj['transform']==f"translate({declared['x']} {declared['y']})"
        assert obj['data-object-id']==declared['id']
    assert fields['drawingId']==d['id'] and fields['revision']==d['revision']
    parsed[(d['id'],d['revision'])]=(d,fields,objects)
latest={}
for d in manifest['drawings']:
    latest.setdefault(d['id'],parsed[(d['id'],d['revision'])])
failures={}
for d,fields,objects in parsed.values():
    issues=[]
    for k in ['drawingId','title','revision','siteId','area','date','scale','size','drawnBy','approvedBy']:
        if not fields.get(k):issues.append('TB-001')
    for o in objects:
        rule=standards.get(o['data-object-type'])
        if not rule or rule['id']!=o['data-standard-id']:issues.append('OBJ-002')
        if rule and rule.get('requiredAsset') and o.get('data-asset-id') not in assets:issues.append('TAG-001')
        if o['data-object-type']=='opc':
            target=latest.get(o['data-target-drawing'])
            endpoint=next((n for n in target[2] if n['data-object-id']==o['data-target-object']),None) if target else None
            if not endpoint or endpoint.get('data-object-type')!='opc' or endpoint.get('data-connection')!=o['data-connection'] or endpoint.get('data-target-drawing')!=d['id'] or endpoint.get('data-target-object')!=o['data-object-id']:issues.append('OPC-001')
    failures[(d['id'],d['revision'])]=issues
    if d['status']=='Released':assert not issues,(d['file'],issues)
assert sorted(failures[('UT-PID-0199','A')])==sorted(['TB-001','TB-001','OBJ-002','TAG-001','OPC-001'])
print('Actual XML verification passed: 7 SVGs; released sheets conform; draft exposes exactly 5 expected violations.')
