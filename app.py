import pandas as pd
import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="สื่อการเรียนรู้: ตรรกศาสตร์คณิตศาสตร์",
    page_icon="🧠",
    layout="wide",
)

st.title("🧠 สื่อการเรียนรู้แบบโต้ตอบ: ตรรกศาสตร์ (Mathematical Logic)")
st.caption("จัดทำขึ้นจากเนื้อหารายวิชา Mathematical Logic (English for Teaching Mathematics)")

# เมนูด้านข้าง
st.sidebar.header("📌 เมนูบทเรียน")
menu = st.sidebar.radio(
    "เลือกหัวข้อที่ต้องการเรียนรู้:",
    [
        "1. ตัวเชื่อมและตารางค่าความจริง (Connectives)",
        "2. การตรวจสอบสัจนิรันดร์ (Tautology)",
        "3. ควิซทดสอบความรู้ (Quiz)",
    ],
)

# -------------------------------------------------------------------
# บทที่ 1: ตัวเชื่อมและตารางค่าความจริง
# -------------------------------------------------------------------
if menu == "1. ตัวเชื่อมและตารางค่าความจริง (Connectives)":
    st.header("📖 1. ตัวเชื่อมทางตรรกศาสตร์ และตารางค่าความจริง")
    st.write("ทดลองเลือกค่าความจริงของประพจน์ $p$ และ $q$ เพื่อดูผลลัพธ์ของตัวเชื่อมต่างๆ")

    col1, col2 = st.columns(2)
    with col1:
        p = st.selectbox("เลือกค่าความจริงของ p:", [True, False], index=0)
    with col2:
        q = st.selectbox("เลือกค่าความจริงของ q:", [True, False], index=0)

    # คำนวณค่าทางตรรกศาสตร์
    not_p = not p
    and_op = p and q
    or_op = p or q
    implies_op = (not p) or q
    iff_op = p == q

    st.subheader("📊 ผลลัพธ์จากการเชื่อมประพจน์")
    result_df = pd.DataFrame(
        {
            "ตัวเชื่อม (Connective)": [
                "นิเสธ (Negation: ~p)",
                "และ (Conjunction: p ∧ q)",
                "หรือ (Disjunction: p ∨ q)",
                "ถ้า...แล้ว (Implication: p → q)",
                "ก็ต่อเมื่อ (Biconditional: p ↔ q)",
            ],
            "ค่าความจริง (Truth Value)": [
                not_p,
                and_op,
                or_op,
                implies_op,
                iff_op,
            ],
        }
    )
    st.table(result_df)

# -------------------------------------------------------------------
# บทที่ 2: สัจนิรันดร์
# -------------------------------------------------------------------
elif menu == "2. การตรวจสอบสัจนิรันดร์ (Tautology)":
    st.header("🔍 2. สัจนิรันดร์ (Tautology)")
    st.write(
        "**สัจนิรันดร์** คือ รูปแบบของประพจน์ที่มีค่าความจริงเป็น **จริง (True)** ในทุกกรณี"
    )

    st.markdown("---")
    st.subheader("💡 ตัวอย่างที่ 1: ตรวจสอบ $(p ∧ q) → (p ∨ q)$")

    if st.button("แสดงตารางค่าความจริงของตัวอย่างนี้"):
        data = []
        for p_val in [True, False]:
            for q_val in [True, False]:
                p_and_q = p_val and q_val
                p_or_q = p_val or q_val
                result = (not p_and_q) or p_or_q
                data.append([p_val, q_val, p_and_q, p_or_q, result])

        df_taut = pd.DataFrame(
            data, columns=["p", "q", "p ∧ q", "p ∨ q", "(p ∧ q) → (p ∨ q)"]
        )
        st.dataframe(df_taut)
        st.success("🎉 ช่องสุดท้ายเป็น จริง (True) ทุกกรณี ดังนั้นประพจน์นี้เป็น **สัจนิรันดร์ (Tautology)**")

# -------------------------------------------------------------------
# บทที่ 3: แบบทดสอบ
# -------------------------------------------------------------------
elif menu == "3. ควิซทดสอบความรู้ (Quiz)":
    st.header("📝 แบบทดสอบความเข้าใจสั้นๆ")

    q1 = st.radio(
        "1. ประพจน์เงื่อนไข $p → q$ จะมีค่าความจริงเป็น **เท็จ (False)** ในกรณีใด?",
        [
            "p เป็นจริง และ q เป็นจริง",
            "p เป็นจริง และ q เป็นเท็จ",
            "p เป็นเท็จ และ q เป็นจริง",
            "p เป็นเท็จ และ q เป็นเท็จ",
        ],
        index=None,
    )

    if st.button("ส่งคำตอบ"):
        if q1 == "p เป็นจริง และ q เป็นเท็จ":
            st.balloons()
            st.success("ถูกต้องแล้วครับ! $T → F$ เป็นกรณีเดียวที่ทำให้เงื่อนไขเป็นเท็จ")
        elif q1 is None:
            st.warning("กรุณาเลือกคำตอบก่อนส่งนะครับ")
        else:
            st.error("ยังไม่ถูกต้อง ลองทบทวนตารางค่าความจริงอีกครั้งนะครับ")
