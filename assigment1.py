import streamlit as st
import random
page_bg_img = '''
<style>
body {
#background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9_eXcz9ATGlyxvAs-3A-NT9SAB7g-qJ8Nsw&usqp=CAU");
background-image: url("https://images.unsplash.com/photo-1429620112901-fe7288646cd3?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


a=['Barcelona','Bayern','Benfica','Chelsea','Juventus','Paris','PSV','Zenit']
b=['Arsenal','Astana','Atletico','Bate','CSKA Moskva','Dinamo Zagreb','Dynamo Kyiv','Galatasary','Gent','Leverkusen','Lyon','M. TEL','Malmo','Man. city','Man. United',
   'Monchengladbach','olympiacosh','porto','Real Madrid','Romo','Sevilla','Shakhtar Donetsk','Valencia','Wolfsburg']
c=['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F',' Group G','Group H' ]
for i in range(0, 8):
   cols = st.beta_columns(5)
   random.shuffle(b)
   random.shuffle(a)
   #st.markdown("<h1 style='text-align: left; color: white;'>cols[0].write(f'{c[i]}')</h1>", unsafe_allow_html=True)
   cols[0].title(f'{c[i]}')
   cols[1].header(f'{a[0]}')
   a.remove(a[0])
   cols[2].header(f'{b[0]}')
   b.remove(b[0])
   cols[3].header(f'{b[0]}')
   b.remove(b[0])
   cols[4].header(f'{b[0]}')
   b.remove(b[0])




