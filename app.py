import streamlit as st

st.title('動画置き場')
st.write('右のセレクトボックスで表示したい動画を選択してください')

option = st.sidebar.selectbox(
    '動画選択',
    ['2022/01/01', '2022/01/02']
)
if option == '2022/01/01':
    st.write('2022/01/01')
    video_file = open('0101.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
else:
    st.write('2022/01/02')
    video_file = open('0102.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
