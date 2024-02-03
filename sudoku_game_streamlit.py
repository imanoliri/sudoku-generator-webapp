import streamlit as st

from sudoku_generator import generate_sudoku


# Run with:
# streamlit run sudoku_game_streamlit.py


## APPLICATION
st.title("Sudoku Generator (Streamlit)")

# Difficulty dropdown
difficulty = st.selectbox("Select Difficulty:", ["Easy", "Medium", "Hard", "Extreme"])

# Button to generate Sudoku board
if st.button("Generate Sudoku"):
    sudoku_board_full, sudoku_board_with_blanks = generate_sudoku(difficulty)
    df_sudoku_full = sudoku_board_full.frame()
    df_sudoku_blanks = sudoku_board_with_blanks.frame().replace(0, "")

    # Display Sudoku board as a table
    st.write("Sudoku Board:")
    st.table(df_sudoku_blanks)
    st.write("Sudoku Board (Solution):")
    st.table(df_sudoku_full)
