import streamlit as st
import pandas as pd
import sympy as sp
import itertools

# ---------------------------------------------------------
# Page Configuration & Style
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mathematical Logic Report App",
    page_icon="📚",
    layout="wide"
)

# Custom CSS สำหรับปรับแต่งความสวยงาม
st.markdown("""
<style>
    .main-title { font-size: 36px; font-weight: bold; color: #1E3A8A; margin-bottom: 0px; }
    .sub-title { font-size: 18px; color: #4B5563; margin-bottom: 20px; }
    .chapter-header { border-left: 5px solid #2563EB; padding-left: 10px; color: #1E40AF; }
    .proof-box { background-color: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 16px; margin-bottom: 16px; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.title("📌 Menu Navigation")
menu = st.sidebar.radio(
    "Go to:",
    [
        "Cover & Overview",
        "Notation & Symbols",
        "Chapter 1: Introduction to Logic",
        "Chapter 2: Connectives & Truth Tables",
        "Chapter 3: Tautologies",
        "Chapter 4: Arguments",
        "Chapter 5: Open Sentences & Quantifiers",
        "Chapter 6: Inductive & Deductive Reasoning",
        "References"
    ]
)

# ---------------------------------------------------------
# Page 1: Cover & Overview
# ---------------------------------------------------------
if menu == "Cover & Overview":
    st.markdown('<p class="main-title">Mathematical Logic Report</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">English for Teaching Mathematics | Semester 1 Academic Year 2026</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        **Prepared by:**
        * Ms. Asma Cheloh (ID 6711070055)
        * Ms. Nur-aima Mahae (ID 671107068)
        
        **Submitted to:**
        * Assistant Professor Dr. litiwat Tocharoennirattisa
        
        **Faculty/Department:**
        * Faculty of Education, Mathematics Department, Rajabhat Thonburi University
        """)
    with col2:
        st.success("""
        ### 📖 Preface Summary
        This report covers fundamental concepts in Mathematical Logic:
        * Propositions and Connectives
        * Truth Tables & Logical Equivalence
        * Tautologies & Contradictions
        * Rules of Inference & Valid Arguments
        * Open Sentences & Quantifiers
        * Inductive & Deductive Proofs
        """)

# ---------------------------------------------------------
# Page 2: Notation & Symbols
# ---------------------------------------------------------
elif menu == "Notation & Symbols":
    st.markdown('<h2 class="chapter-header">Notation and Proof Conventions</h2>', unsafe_allow_html=True)
    
    symbol_data = {
        "Symbol": ["p, q, r, s, t", "¬", "∧", "∨", "→", "↔", "T / F", "⊢", "⊨", "∀ / ∃"],
        "Meaning": [
            "Atomic propositions",
            "Negation (Not)",
            "Conjunction (And)",
            "Inclusive disjunction (Or)",
            "Material implication (If...then)",
            "Biconditional (If and only if)",
            "Truth values: True / False",
            "Syntactic derivability (Provable)",
            "Semantic entailment (Valid)",
            "Universal and Existential quantifiers"
        ]
    }
    st.table(pd.DataFrame(symbol_data))

# ---------------------------------------------------------
# Chapter 1: Introduction to Mathematical Logic
# ---------------------------------------------------------
elif menu == "Chapter 1: Introduction to Logic":
    st.markdown('<h2 class="chapter-header">Chapter 1: Introduction to Mathematical Logic</h2>', unsafe_allow_html=True)
    
    st.write("""
    **Definitions & Central Ideas:**
    Mathematical logic studies the formal structure of valid reasoning. A proposition has exactly one truth value, true or false. 
    Atomic propositions are represented by $p, q, r, s$; compound propositions are formed using connectives.
    """)
    
    st.markdown("### 📝 Advanced Worked Proofs")
    
    with st.expander("Proof 1.1: Chained Inference with 4 Propositions"):
        st.markdown("""
        * **Premises:** $p \\rightarrow q; \\quad q \\rightarrow r; \\quad r \\rightarrow s; \\quad p$
        * **Prove:** $s$
        * **Proof:**
            1. From $p$ and $p \\rightarrow q$, infer $q$ *(Modus Ponens)*
            2. From $q$ and $q \\rightarrow r$, infer $r$ *(Modus Ponens)*
            3. From $r$ and $r \\rightarrow s$, infer $s$ *(Modus Ponens)*
            4. Therefore, the conclusion $s$ follows from the premises.
        """)

    with st.expander("Proof 1.2: Indirect Proof Using Three Atoms"):
        st.markdown("""
        * **Premises:** $p \\vee q; \\quad p \\rightarrow r; \\quad q \\rightarrow r$
        * **Prove:** $r$
        * **Proof:**
            1. Assume $\\neg r$ for contradiction.
            2. By Modus Tollens on $p \\rightarrow r$ and $\\neg r$, infer $\\neg p$.
            3. From $p \\vee q$ and $\\neg p$, infer $q$.
            4. By Modus Tollens on $q \\rightarrow r$ and $\\neg r$, infer $\\neg q$ (Contradiction with $q$).
            5. Discharge assumption and conclude $r$.
        """)

# ---------------------------------------------------------
# Chapter 2: Logical Connectives and Truth Tables
# ---------------------------------------------------------
elif menu == "Chapter 2: Connectives & Truth Tables":
    st.markdown('<h2 class="chapter-header">Chapter 2: Logical Connectives and Truth Tables</h2>', unsafe_allow_html=True)
    
    st.write("""
    **Useful Identities:**
    * $A \\rightarrow B \\equiv \\neg A \\vee B$
    * De Morgan's Laws: $\\neg(A \\wedge B) \\equiv \\neg A \\vee \\neg B$ and $\\neg(A \\vee B) \\equiv \\neg A \\wedge \\neg B$
    """)
    
    st.subheader("⚡ Interactive Truth Table Generator")
    expr_text = st.text_input("Enter proposition in Python logic syntax (e.g. (p & q) >> r):", value="(p & q) >> r")
    st.caption("Syntax guide: `&` (AND), `|` (OR), `~` (NOT), `>>` (IMPLIES)")
    
    if st.button("Generate Table"):
        try:
            expr = sp.sympify(expr_text)
            vars_sorted = sorted([str(s) for s in expr.free_symbols])
            combos = list(itertools.product([True, False], repeat=len(vars_sorted)))
            rows = []
            for c in combos:
                val_map = dict(zip([sp.Symbol(v) for v in vars_sorted], c))
                res = bool(expr.subs(val_map))
                rows.append(list(c) + [res])
            
            df_res = pd.DataFrame(rows, columns=vars_sorted + ["Result"])
            st.dataframe(df_res, use_container_width=True)
        except Exception as e:
            st.error(f"Error evaluating expression: {e}")

# ---------------------------------------------------------
# Chapter 3: Tautologies
# ---------------------------------------------------------
elif menu == "Chapter 3: Tautologies":
    st.markdown('<h2 class="chapter-header">Chapter 3: Tautologies</h2>', unsafe_allow_html=True)
    
    st.write("""
    * **Tautology:** True under every truth assignment.
    * **Contradiction:** False under every truth assignment.
    * **Contingency:** True under some assignments, false under others.
    """)
    
    st.subheader("🧪 Worked Example: Tautology Checking")
    
    ex_choice = st.selectbox("Select Example from Report:", [
        "Example 1: (p ∧ q) → [(p ∨ q) → r]",
        "Example 2: [(p ∧ q) → (p ∨ q)] ↔ [(~p ∧ ~q) → (~p ∨ ~q)]",
        "Example 3: [(~p ∧ q) → (~q ∧ r)] → (~r ∧ s)",
        "Example 4: [(p ∧ q) → r] ↔ [p → (q → r)]"
    ])
    
    if ex_choice == "Example 1: (p ∧ q) → [(p ∨ q) → r]":
        st.warning("❌ **Result:** Not a Tautology (Counterexample: p=T, q=T, r=F makes the statement False).")
    elif ex_choice == "Example 2: [(p ∧ q) → (p ∨ q)] ↔ [(~p ∧ ~q) → (~p ∨ ~q)]":
        st.success("✅ **Result:** Tautology (Always True).")
    elif ex_choice == "Example 3: [(~p ∧ q) → (~q ∧ r)] → (~r ∧ s)":
        st.success("✅ **Result:** Tautology (Contradiction found when assuming False).")
    elif ex_choice == "Example 4: [(p ∧ q) → r] ↔ [p → (q → r)]":
        st.success("✅ **Result:** Tautology (Logical Equivalence holds in all cases).")

# ---------------------------------------------------------
# Chapter 4: Arguments
# ---------------------------------------------------------
elif menu == "Chapter 4: Arguments":
    st.markdown('<h2 class="chapter-header">Chapter 4: Arguments</h2>', unsafe_allow_html=True)
    
    st.write("An argument consists of premises and a conclusion. An argument is **valid** if every interpretation satisfying the premises also satisfies the conclusion.")
    
    st.markdown("### 🏛️ Key Valid Patterns")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Modus Ponens:** $A \\rightarrow B, A \\vdash B$")
        st.write("**Modus Tollens:** $A \\rightarrow B, \\neg B \\vdash \\neg A$")
    with col2:
        st.write("**Hypothetical Syllogism:** $A \\rightarrow B, B \\rightarrow C \\vdash A \\rightarrow C$")
        st.write("**Disjunctive Syllogism:** $A \\vee B, \\neg A \\vdash B$")

    st.markdown("### 📝 Proof 4.1 Example")
    st.code("""
    Premises:
    1. p ∨ q
    2. p → r
    3. q → s
    4. ~r
    Prove: s
    
    Proof Steps:
    1. From (p → r) and ~r, infer ~p (Modus Tollens)
    2. From (p ∨ q) and ~p, infer q (Disjunctive Syllogism)
    3. From (q → s) and q, infer s (Modus Ponens)
    Conclusion: s is Valid!
    """, language="text")

# ---------------------------------------------------------
# Chapter 5: Open Sentences & Quantifiers
# ---------------------------------------------------------
elif menu == "Chapter 5: Open Sentences & Quantifiers":
    st.markdown('<h2 class="chapter-header">Chapter 5: Open Sentences and Quantifiers</h2>', unsafe_allow_html=True)
    
    st.write("""
    * **Universal Quantifier ($\forall x$):** States that $P(x)$ holds for ALL elements in the domain.
    * **Existential Quantifier ($\exists x$):** States that $P(x)$ holds for AT LEAST ONE element in the domain.
    """)
    
    st.info("""
    **Quantifier Negation Laws:**
    * $\\neg \\forall x P(x) \\equiv \\exists x \\neg P(x)$
    * $\\neg \\exists x P(x) \\equiv \\forall x \\neg P(x)$
    """)
    
    st.markdown("### ⚠️ Order of Quantifiers Matters!")
    st.write("Over integers $\\mathbb{Z}$:")
    st.write("1. $\\forall x \\exists y (x < y)$ is **TRUE** (Choice: $y = x + 1$).")
    st.write("2. $\\exists y \\forall x (x < y)$ is **FALSE** (No single integer is strictly greater than all integers).")

# ---------------------------------------------------------
# Chapter 6: Inductive and Deductive Reasoning
# ---------------------------------------------------------
elif menu == "Chapter 6: Inductive & Deductive Reasoning":
    st.markdown('<h2 class="chapter-header">Chapter 6: Inductive and Deductive Reasoning</h2>', unsafe_allow_html=True)
    
    st.write("""
    * **Inductive Reasoning:** Generalizes from specific observations.
    * **Deductive Reasoning:** Establishes conclusions that necessarily follow from premises.
    * **Mathematical Induction:** A formal deductive proof technique for claims over positive integers.
    """)
    
    st.subheader("🔢 Mathematical Induction Interactive Calculator")
    st.write("Claim: $1^3 + 2^3 + 3^3 + \\dots + n^3 = \\left[ \\frac{n(n+1)}{2} \\right]^2$")
    
    n_input = st.slider("Select value for n:", min_value=1, max_value=20, value=5)
    
    left_hand = sum([i**3 for i in range(1, n_input + 1)])
    right_hand = int((n_input * (n_input + 1) / 2) ** 2)
    
    c1, c2 = st.columns(2)
    c1.metric("LHS (Sum of Cubes)", left_hand)
    c2.metric("RHS ([n(n+1)/2]²)", right_hand)
    
    if left_hand == right_hand:
        st.success(f"✅ Verified for n = {n_input}! LHS equals RHS.")

# ---------------------------------------------------------
# Page: References
# ---------------------------------------------------------
elif menu == "References":
    st.markdown('<h2 class="chapter-header">References</h2>', unsafe_allow_html=True)
    st.markdown("""
    * **Epp, S. S. (2011).** *Discrete Mathematics with Applications* (4th ed.). Brooks/Cole.
    * **Rosen, K. H. (2019).** *Discrete Mathematics and Its Applications* (8th ed.). McGraw-Hill Education.
    * **Enderton, H. B. (2001).** *A Mathematical Introduction to Logic* (2nd ed.). Academic Press.
    * **Velleman, D. J. (2019).** *How to Prove It: A Structured Approach* (3rd ed.). Cambridge University Press.
    """)
