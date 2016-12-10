# UnityResourceChecker
This's small tool I write for my project to help me easier to track assets depenedencies.
It's useful when you have a lot of particles, materials, textures linked with each other and you're afraid of removing any assets will affect others.

Requirement:
- You have to install Python in order to use.
- Why i use python ?
 -> Python deals with string and files much better than Unity does.
 
How to use:
- Right Click -> Select texture -> FindMaterialsAndPrefabsByTexture
- Right Click -> Select material -> FindPrefabsByMaterial
- Output format is json.

Hopy you may find it useful for your project :)
