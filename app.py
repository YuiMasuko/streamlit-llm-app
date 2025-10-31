from dotenv import load_dotenv

load_dotenv()

# ライブラリをインポート
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage


# LLMからの回答を取得する関数
def get_ai_response(input_text, selected_role):

    # LLMのインスタンスを作成
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)
    
    # 選択された相談相手に応じてシステムメッセージを変更
    if selected_role == "大学の先生":
        system_message = "あなたは大学の先生です。学生の進路相談に対して、学術的な視点や教育者としての経験から親身にアドバイスをしてください。"
    else:
        system_message = "あなたは社会人アドバイザーです。実際の社会経験や職場での経験を踏まえて、実践的なアドバイスをしてください。"
    
    # メッセージのリストを作成
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]
    
    # LLMに問い合わせて結果を取得
    result = llm(messages)
    
    # 回答内容を返す
    return result.content


# アプリのタイトル表示
st.title("進路相談AI")

# アプリの説明文を表示
st.markdown("""
将来の進路に迷ったとき、大学の先生と社会人の2人の視点から話を聞けるAIです。
どちらに相談したいかを選んで、今の気持ちを入力してみてください。
""")

# ユーザーに選択させるラジオボタン
selected_item = st.radio(
    "相談相手を選んでください",
    ["大学の先生", "社会人アドバイザー"]
)

# テキスト入力フィールドを作成
input_message = st.text_input(label="あなたの悩みを入力してください")

# 区切り線を表示
st.divider()

# 「相談する」ボタンが押されたときの処理
if st.button("相談する"):
    st.divider()
    
    # 入力テキストがあるかチェック
    if input_message:
        # 選択された相談相手を表示
        if selected_item == "大学の先生":
            st.write("**大学の先生に相談します**")
        else:
            st.write("**社会人アドバイザーに相談します**")
        
        # LLMから回答を取得
        response = get_ai_response(input_message, selected_item)
        
        # 回答を画面に表示
        st.write("#### 回答:")
        st.write(response)
    
    else:
        # エラーメッセージを表示
        st.error("相談内容を入力してから「相談する」ボタンを押してください。")