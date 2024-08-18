import streamlit as st
from PIL import Image, ImageFilter


def page_1():
    """music—go"""
    # with open('罗蕾莱的鬼魂.mp3', 'rb') as f:
    #     my_mp3 = f.read()
    st.markdown("<p style='font-family: 演示夏行楷, sans-serif;font-size: 36px; color: lightblue;'>music-go!</p>", unsafe_allow_html=True)
    st.audio('罗蕾莱的鬼魂.mp3', format='audio/mp3', start_time=0)
    st.write('罗蕾莱的鬼魂')
    st.audio('星星和我们.mp3', format='audio/mp3', start_time=0)
    st.write('星星和我们')
    st.audio('AloneToAlone.mp3', format='audio/mp3', start_time=0)
    st.write("Alone To Alone")
    st.audio('鸟之诗.mp3', format='audio/mp3', start_time=0)
    st.write("鸟之诗")
    st.write('——————————————————————————')

def page_2():
    """man画"""
    st.markdown("<p style='font-family: 演示夏行楷, sans-serif;font-size: 36px; color: black;'>man画</p>", unsafe_allow_html=True)
    st.write('Part1--Eva')
    st.image('望妻.jpg')
    st.write('——————————————————————————')
    st.image('渚薰独照.jpg')
    st.write('——————————————————————————')
    st.image('真嗣护香.jpg')
    st.write('——————————————————————————')
def page_3():
    st.markdown("<p style='font-family: 演示夏行楷, sans-serif;font-size: 36px; color: red;'>图片处理工具</p>", unsafe_allow_html=True)
    """我的图片处理工具"""
    uploaded_file = st.file_uploader('上传图片',type = ['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)

        col1, col2, col3 = st.columns([3, 2, 4])
        with col1:
            st.image(img)
        with col2:
            ch = st.toggle('高斯模糊')
            co = st.toggle('锐化')
            bw = st.toggle('边缘增强')
        with col3:
            st.write('对图片进行模糊处理')
            st.write('让图片锐化')
            st.write('将图片边缘突出')
        # 点击按钮处理图片
        b = st.button('开始处理')
        if b:
            if ch:
                st.image(img.filter(ImageFilter.GaussianBlur(radius=5)))
            if co:
                st.image(img.filter(ImageFilter.SHARPEN))
            if bw:
                st.image(img.filter(ImageFilter.EDGE_ENHANCE))
            st.write('右键"另存为"保存图片')
            st.image(img)
        # st.image(img)
        # st.image(img_change(img,0,2,1))

        # tab1,tab2,tab3,tab4 = st.tabs(['原图','高斯模糊','锐化','边缘增强'])
        # with tab1:
        #     st.image(img)
        # with tab2:
        #     st.image(img.filter(ImageFilter.GaussianBlur(radius=5)))
        # with tab3:
        #     st.image(img.filter(ImageFilter.SHARPEN))
        # with tab4:
        #     st.image(img.filter(ImageFilter.EDGE_ENHANCE))
def img_change(img,rc,gc,bc):
    """图片处理"""
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
def page_4():
    st.markdown("<p style='font-family: 演示夏行楷, sans-serif;font-size: 36px; color: lightblue;'>智慧词典</p>", unsafe_allow_html=True)
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    word = st.text_input('请输入要查询的单词')
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])

    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：',times_dict[n])
        if word == 'apple':
            st.code("""
                    wow~ ~,apple!""")
# def page_5():
#     st.markdown("<p style='font-family: 演示夏行楷, sans-serif;font-size: 36px; color: green;'>留言区</p>", unsafe_allow_html=True)
#     with open('leave_messages.txt',"r",encoding='utf-8') as f:
#         messages_list = f.read().split('\n')
#     for  i in range(len(messages_list)):
#         messages_list[i] = messages_list[i].split('#')
#     for i in messages_list:
#         if i[1] == '阿短':
#             with st.chat_message('🟡'):
#                 st.write(i[1],':',i[2])
#         elif i[1] == '编程猫':
#             with st.chat_message('🟥'):
#                 st.write(i[1],':',i[2])
#     name = st.selectbox('我是...',['阿短','编程猫'])
#     new_message = st.text_input('想要说的话......')
#     if st.button('留言'):
#         messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
#         with open('leave_messages.txt','w',encoding='utf-8') as f:
#             message = ''
#             for i in messages_list:
#                 message += i[0] + '#' +i[1] + '#' + i[2] + '\n'
#             message = message[:-1]
#             f.write(message)
def page_no():
    st.write('Oh,there is nothing!')
    st.image('LongTu.jpg')
# 侧边栏选择
st.sidebar.markdown("<h1 style='font-size: 24px; color: green;'>我的小屋</h1>", unsafe_allow_html=True)
page = st.sidebar.radio("————————", ['music—go', 'man画','图片处理','我的智慧词典'])

# 根据选择显示页面内容
if page == 'music—go':
    page_1()
elif page == 'man画':
    page_2()
elif page == '图片处理':
    page_3()
elif page == '我的智慧词典':
    page_4()
# elif page == '我的留言区':
#     page_5()

