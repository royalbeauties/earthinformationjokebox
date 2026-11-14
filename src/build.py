import base64, json, os
HERE=os.path.dirname(os.path.abspath(__file__)); ASSETS=os.path.join(HERE,'..','assets')
b64=lambda p:'data:image/jpeg;base64,'+base64.b64encode(open(os.path.join(ASSETS,p),'rb').read()).decode()
EIC='NASA Earth Information Center (EIC) visualization'
P=[
 ('y2012','earth','Night Lights 2012','Earth at night','Earth at night in 2012. Each little light is a city or a town, seen by satellites from space.',EIC,'eic/y2012.jpg'),
 ('y2023','earth','Night Lights 2023','Eleven years later','Earth at night in 2023. Can you spot more lights than in 2012?',EIC,'eic/y2023.jpg'),
 ('change_world','earth','Lights Out & New Lights','How night lights changed','This map shows how night lights changed from 2012 to 2023. Purple = new lights. Orange = less light. White = about the same.',EIC,'eic/change_world.jpg'),
 ('india_lights','earth','India at Night 2023','Cities and roads glowing','India at night in 2023. Bright dots are big cities, and the lines of light follow roads and towns.',EIC,'eic/india_lights.jpg'),
 ('india_change','earth','India: New Lights','So much purple!','Lots of purple! Many new lights appeared in India between 2012 and 2023.',EIC,'eic/india_change.jpg'),
 ('europe_change','earth','Europe: Light Change','Lots of orange','In much of Western Europe, satellites saw less light (orange) in 2023 than in 2012.',EIC,'eic/europe_change.jpg'),
 ('nile_change','earth','The Nile: Light Change','A ribbon of light','The river Nile glows like a ribbon of light through the desert. Purple shows new lights, orange shows less light.',EIC,'eic/nile_change.jpg'),
 ('earth_iss','earth','Earth from the Space Station','Night side of Earth','Astronauts on the International Space Station took this photo at night. The green line is <b>airglow</b>: air high above Earth gently glowing. Canadian astronaut Julie Payette visited this space station.','NASA / ISS crew','pics/earth_iss.jpg'),
 ('cartwheel','space','Cartwheel Galaxy','A galaxy shaped like a wheel','The Cartwheel Galaxy looks like a giant wagon wheel. Long ago a smaller galaxy zoomed through it and made the ring.','NASA, ESA, CSA, STScI (Webb)','pics/cartwheel.jpg'),
 ('sun','space','Our Sun','Our closest star','This is our Sun, photographed by a NASA spacecraft that watches it all day. The bright loops are super-hot gas.','NASA Solar Dynamics Observatory','pics/sun.jpg'),
 ('flare','space','Solar Flare','A burst of energy on the Sun','A solar flare is a giant flash of light and energy on the Sun.','NASA Solar Dynamics Observatory','pics/flare.jpg'),
 ('casa','space','Cassiopeia A','Leftovers of an exploded star','Cassiopeia A is what is left after a giant star exploded (a supernova). The colours show different kinds of light.','NASA telescopes (Chandra and others)','pics/casa.jpg'),
]
pics=[dict(id=i,group=g,title=t,short=s,fact=f,credit=c,src=b64(p)) for i,g,t,s,f,c,p in P]
years={'world':[dict(year=y, src=(pics[0]['src'] if y==2012 else pics[1]['src'] if y==2023 else b64(f'eic/y{y}.jpg'))) for y in range(2012,2024)]}
for r in ['india','europe','nile']: years[r]=[dict(year=y,src=b64(f'eic/years_closeups/{r}{y}.jpg')) for y in range(2012,2024)]
t=open(os.path.join(HERE,'template.html')).read().replace('__PICS__',json.dumps(pics)).replace('__YEARS__',json.dumps(years))
open(os.path.join(HERE,'..','index.html'),'w').write(t); print(len(t)//1024,'KB')
