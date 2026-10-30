import {cpSync,rmSync,mkdirSync,writeFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import './generate-drawings.mjs';
const root=fileURLToPath(new URL('../',import.meta.url));
mkdirSync(path.join(root,'dist'),{recursive:true});
for(const f of ['index.html','app.js','domain.js','xml.js','catalog.js','style.css']){
 cpSync(path.join(root,'src',f),path.join(root,'dist',f));
 cpSync(path.join(root,'src',f),path.join(root,f));
}
cpSync(path.join(root,'drawings'),path.join(root,'dist/drawings'),{recursive:true});
writeFileSync(path.join(root,'.nojekyll'),'');
console.log('Prepared main / (root) publication and dist preview.');
