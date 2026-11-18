


import random
import streamlit as st

# 1. 网页基本设置
st.set_page_config(
    page_title="MealMate - 今天吃什么",
    page_icon="🍜"
)

# 2. 菜品数据库
foods = [
    {"name": "包子", "meal": "早餐", "price": 5, "description": "经典早餐"},
    {"name": "豆浆油条", "meal": "早餐", "price": 7, "description": "中式早餐"},
    {"name": "鸡蛋饼", "meal": "早餐", "price": 8, "description": "香脆可口"},
    {"name": "煎饺", "meal": "早餐", "price": 10, "description": "外脆里嫩"},
    {"name": "牛肉面", "meal": "正餐", "price": 16, "description": "汤鲜味美"},
    {"name": "黄焖鸡米饭", "meal": "正餐", "price": 18, "description": "下饭首选"},
    {"name": "番茄鸡蛋面", "meal": "正餐", "price": 12, "description": "酸甜开胃"},
    {"name": "鸡腿饭", "meal": "正餐", "price": 15, "description": "营养丰富"},
    {"name": "麻辣烫", "meal": "正餐", "price": 30, "description": "食材丰富"},
    {"name": "兰州拉面", "meal": "正餐", "price": 12, "description": "经典面食"},
    {"name": "兰州拉面", "meal": "早餐", "price": 12, "description": "经典面食"},
    {"name": "牛肉面", "meal": "早餐", "price": 16, "description": "汤鲜味美"},
    {"name": "炒饭", "meal": "正餐", "price": 12, "description": "简单美味"},
    {"name": "盖浇饭", "meal": "正餐", "price": 16, "description": "饱腹感强"},
    {"name": "猪脚饭", "meal": "正餐", "price": 15, "description": "香浓软糯"},
    {"name": "螺蛳粉", "meal": "正餐", "price": 12, "description": "酸辣鲜香"},
    {"name": "饺子", "meal": "正餐", "price": 16, "description": "经典面食"},
    {"name": "意大利面", "meal": "正餐", "price": 20, "description": "经典面食"},
    {"name": "泡面", "meal": "正餐", "price": 5, "description": "省钱"},
    {"name": "干锅鸡", "meal": "正餐", "price": 20, "description": "外焦里嫩"},
    {"name": "鸡公煲", "meal": "正餐", "price": 20, "description": "食材丰富"},
    {"name": "米线", "meal": "正餐", "price": 15, "description": "经典面食"},
    {"name": "米线", "meal": "早餐", "price": 15, "description": "经典面食"},
    {"name": "饺子", "meal": "早餐", "price": 16, "description": "经典面食"},
    {"name": "食堂", "meal": "正餐", "price": 10, "description": "省钱"},
    {"name": "烤鸭", "meal": "正餐", "price": 25, "description": "外脆里嫩"},
    {"name": "火锅", "meal": "正餐", "price": 50, "description": "食材丰富"},
    {"name": "烤肉", "meal": "正餐", "price": 50, "description": "外焦里嫩"},
    {"name": "KFC", "meal": "正餐", "price": 50, "description": "好吃"},
    {"name": "披萨", "meal": "正餐", "price": 40, "description": "好吃"},
    {"name": "麦当劳", "meal": "正餐", "price": 35, "description": "好吃"},
    {"name": "塔斯汀", "meal": "正餐", "price": 35, "description": "好吃"},
    {"name": "蛋糕", "meal": "正餐", "price": 45, "description": "好吃"},

]

# 3. 网页标题
st.title("🍜 MealMate")
st.subheader("今天吃什么？")
st.write("告别选择困难，让我帮你决定今天吃什么！")

st.divider()

# 4. 选择用餐时间
meal = st.selectbox(
    "你现在准备吃哪一餐？",
    ["早餐", "正餐（午餐/晚餐）"],
    key="meal_selector"
)

# 5. 设置预算
# 根据用餐类型设置最高预算
if meal == "早餐":
    max_budget = 20
    default_budget = 15
else:
    max_budget = 50
    default_budget = 30

budget = st.slider(
    "你的预算是多少？",
    min_value=5,
    max_value=max_budget,
    value=default_budget,
    step=1
)
min_ratio = st.slider(
    "最低消费比例",
    min_value=50,
    max_value=90,
    value=70,
    step=5,
    format="%d%%"
)

min_price = budget * min_ratio / 100

st.write(f"当前选择：{meal}，预算：{budget} 元")

# 6. 推荐按钮
if st.button("🍜 帮我推荐"):

    # 根据用餐时间和预算筛选菜品
    available_foods = [
        food for food in foods
        if (
                   (
                           meal == "正餐（午餐/晚餐）"
                           and food["meal"] == "正餐"
                   )
                   or (
                           meal == "早餐"
                           and food["meal"] == "早餐"
                   )
           )
           and min_price<=food["price"] <= budget
    ]

    # 判断有没有符合条件的菜品
    if available_foods:
        result = random.choice(available_foods)
        st.session_state["result"] = result
        st.session_state["result_key"] = (meal, budget)
    else:
        st.session_state["result"] = None
        st.session_state["result_key"] = (meal, budget)

# 7. 展示推荐结果
if st.session_state.get("result_key") == (meal, budget):

    result = st.session_state.get("result")

    if result:
        st.success("🎉 今天推荐你吃：")

        st.title(f"🍽️ {result['name']}")

        st.write(f"价格：{result['price']} 元")
        st.write(f"介绍：{result['description']}")

        st.info("这道菜符合你设置的预算！")

    else:
        st.warning("没有找到符合预算的菜品，可以适当提高预算。")
