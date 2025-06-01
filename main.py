import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# 12. プレグレスバーの表示

st.write('プログレスバーの表示')
'Start!!'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!!'

# 9. Streamlitの基本的な使い方
st.title('Streamlit 超入門')

st.write('Dataframe')

df=pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10, 20, 30, 40]
})

st.write(df)
st.dataframe(df.style.highlight_max(axis=0),width=1000, height=200)
st.table(df.style.highlight_max(axis=0))


"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

df2=pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df3=pd.DataFrame(
    np.random.rand(100,2)/[50, 50]+[35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df3)

st.write('Display Image')

img=Image.open('sample.jpg')
st.image(img, caption='Yuki', use_container_width=True)

# 10. インタラクティブなウィジェット
if st.checkbox('ShowImage'):
    img2=Image.open('sample.jpg')
    st.image(img2, caption='Yuki2', use_container_width=True)

option=st.selectbox(
    'あなたが好きな数字を教えてください。', 
    list(range(1,11))
)
'あなたの好きな数字は', option, 'です。'

# text=st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味は', text, 'です。'

# condition=st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition

# 11. レイアウトを整える
st.sidebar.write('Layout')

text2=st.sidebar.text_input('あなたの趣味を教えてください。')
'あなたの趣味は', text2, 'です。'

condition2=st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition2

left_column, right_column=st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander=st.expander('問い合わせ1')
expander.write('問い合わせ内容を書く')
expander=st.expander('問い合わせ2')
expander.write('問い合わせ内容を書く')
expander=st.expander('問い合わせ3')
expander.write('問い合わせ内容を書く')

# 13. Webアプリの公開