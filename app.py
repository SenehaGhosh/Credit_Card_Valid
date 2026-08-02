import streamlit as st
import re

st.set_page_config(
    page_title="Credit Card Validator",
    page_icon="💳",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb);
background-attachment:fixed;
}

.main-title{
text-align:center;
color:white;
font-size:40px;
font-weight:bold;
margin-bottom:5px;
}

.subtitle{
text-align:center;
color:#E5E7EB;
font-size:18px;
margin-bottom:25px;
}

.card-box{
background:white;
padding:30px;
border-radius:20px;
box-shadow:0px 8px 25px rgba(0,0,0,0.25);
}

.credit-card{
background:linear-gradient(135deg,#111827,#2563EB);
border-radius:18px;
padding:25px;
color:white;
margin-bottom:25px;
box-shadow:0px 8px 20px rgba(0,0,0,0.4);
}

.card-number{
font-size:24px;
letter-spacing:3px;
margin-top:25px;
margin-bottom:20px;
font-weight:bold;
}

.small-text{
font-size:13px;
color:#D1D5DB;
}

.card-type{
float:right;
font-size:20px;
font-weight:bold;
}

.stButton>button{
width:100%;
background:#2563EB;
color:white;
font-size:18px;
border-radius:12px;
padding:12px;
border:none;
font-weight:bold;
}

.stButton>button:hover{
background:#1D4ED8;
color:white;
}

</style>
""", unsafe_allow_html=True)


def validate_card(card):

    card = card.replace(" ", "").replace("-", "")

    if not card.isdigit():
        return False

    total = 0

    reverse_digits = card[::-1]

    for i, digit in enumerate(reverse_digits):

        n = int(digit)

        if i % 2 == 1:
            n *= 2

            if n > 9:
                n -= 9

        total += n

    return total % 10 == 0


def detect_card_type(number):

    if number.startswith("4"):
        return "VISA"

    elif re.match(r"^5[1-5]", number):
        return "MASTERCARD"

    elif number.startswith("34") or number.startswith("37"):
        return "AMEX"

    elif number.startswith("60") or number.startswith("65"):
        return "RUPAY"

    else:
        return "UNKNOWN"


st.markdown(
'<h1 class="main-title">💳 Credit Card Validator</h1>',
unsafe_allow_html=True)

st.markdown(
'<p class="subtitle">Validate your card instantly using the Luhn Algorithm</p>',
unsafe_allow_html=True)

card = st.text_input(
"Enter Card Number",
max_chars=19,
placeholder="1234 5678 9012 3456"
)

number = card.replace(" ", "").replace("-", "")

display = card if card else "**** **** **** ****"

ctype = detect_card_type(number)

st.markdown(f"""
<div class="credit-card">

<div class="card-type">
{ctype}
</div>

<div class="small-text">
Credit Card
</div>

<div class="card-number">
{display}
</div>

<div class="small-text">
Powered by Luhn Algorithm
</div>

</div>
""", unsafe_allow_html=True)
# ---------- Validation Section ----------

st.markdown(
    '<div class="card-box">',
    unsafe_allow_html=True
)

if st.button("🔍 Validate Card"):

    if number == "":
        st.warning("⚠️ Please enter a card number.")

    elif len(number) < 13:
        st.warning("⚠️ Card number should contain at least 13 digits.")

    elif len(number) > 19:
        st.warning("⚠️ Card number is too long.")

    elif validate_card(number):

        st.success("✅ Valid Credit Card Number")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Card Length",
                f"{len(number)} digits"
            )

        with col2:
            st.metric(
                "Card Type",
                detect_card_type(number)
            )

        st.info(
            "This card number passed the Luhn Algorithm check."
        )

    else:

        st.error("❌ Invalid Credit Card Number")

        st.warning(
            "Please check the entered number and try again."
        )


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# ---------- Information Section ----------

st.divider()

st.subheader("🔐 About This Validator")

st.write(
"""
- Uses the **Luhn Algorithm** for validation.
- Does not store or save your card number.
- Works only as a mathematical validation tool.
- No real payment verification is performed.
"""
)


st.divider()

st.caption(
    "Built with ❤️ using Python and Streamlit"
)