import streamlit as st

def compare_answers(student_answer, model_answer):
    student_words = set(student_answer.lower().split())
    model_words = set(model_answer.lower().split())
    correct_words = student_words.intersection(model_words)
    missing_words = model_words - student_words
    
    match = len(correct_words) / len(model_words) > 0.7  # If at least 70% match
    improvement_suggestions = f"✅ Words you included: {', '.join(correct_words)}\n❌ Words you missed: {', '.join(missing_words)}"
    
    return {"match": match, "improvement_suggestions": improvement_suggestions}

def main():
    st.title("Harrison Bergeron - Understanding & Analysis Quiz")
    
    # Provide text access
    with st.expander("Read this part of the story"):
        st.markdown("""
        **Harrison Bergeron** is a story about a world where everyone is forced to be equal.
        """)
    
    st.header("Answer the Question Below")
    
    # Define model answer
    model_answer = ("The handicaps in Harrison Bergeron are designed to enforce absolute equality by suppressing any "
                    "natural advantages individuals may have. For instance, those with above-average intelligence, like "
                    "George Bergeron, must wear mental handicap radios that emit disruptive noises, preventing them from "
                    "thinking deeply. Physically strong individuals, such as Harrison himself, carry immense weights to limit "
                    "their strength, while the beautiful must wear grotesque masks to obscure their attractiveness. These "
                    "handicaps ensure that no one is superior to another in any way, reflecting an extreme and oppressive "
                    "interpretation of equality.")
    
    # Step 1: Open-ended Question
    response_key = "Q1_response"
    if response_key not in st.session_state:
        st.session_state[response_key] = ""
    response = st.text_area("What is the purpose of the handicaps used in the society of Harrison Bergeron? Give examples of different types of handicaps used:", key=response_key)
    
    if response:
        # Store initial response
        if "initial_response" not in st.session_state:
            st.session_state["initial_response"] = response
        
        # Check if the answer is similar to the model answer
        similarity_feedback = compare_answers(response, model_answer)
        
        if similarity_feedback["match"]:
            st.success("✅ Great response! Here is some feedback on how you can improve your academic style and clarity:")
            st.write(similarity_feedback["improvement_suggestions"])
        else:
            st.warning("Your response could be improved. Let’s go step by step. There are two parts to this section, each should be written in clear, concise, academic style.")
            
            # Provide First Section of Text for Scaffolding
            st.subheader("Re-read This Section")
            st.markdown("*Nobody was smarter than anybody else. Nobody was better looking than anybody else. Nobody was stronger or quicker than anybody else.*")
            
            # Step 2: Summarizing the "Nobody was..." Section
            st.subheader("Summarize This Section")
            summary_response = st.text_area("Use this sentence starter to summarize: In this society, the government uses handicaps or devices to make sure that...", key="summary_nobody_was")
            
            if summary_response:
                if "same intelligence" in summary_response.lower() and "same beauty" in summary_response.lower() and "same strength" in summary_response.lower():
                    st.success("✅ Great job! Your summary includes the key points from the text.")
                else:
                    st.warning("Your summary is missing some key points. Make sure you mention intelligence, beauty, and strength.")
        
        # Ask students to rewrite their answer incorporating both elements
        st.subheader("Rewrite Your Answer")
        rewritten_answer = st.text_area("Now, rewrite your answer to the original question: 'What is the purpose of the handicaps used in the society of Harrison Bergeron? Give examples of different types of handicaps used.' Combine your previous two answers into a more complete response:", key="rewritten_answer")
        
        if rewritten_answer:
            st.subheader("Compare Your Answers")
            st.write("**Your First Answer:**")
            st.markdown(f"{st.session_state['initial_response']}")
            st.write("**Your Revised Answer:**")
            st.markdown(f"{rewritten_answer}")
            
            # Compare with Model Answer
            st.subheader("Compare with Model Answer")
            st.markdown(f"**Model Answer:** *{model_answer}*")
            
            improvements = []
            if len(rewritten_answer) > len(st.session_state["initial_response"]):
                improvements.append("Your new answer is more detailed than your first attempt.")
            if "prevent" in rewritten_answer or "limit" in rewritten_answer:
                improvements.append("You have correctly included the purpose behind the handicaps.")
            if "radio" in rewritten_answer or "weights" in rewritten_answer:
                improvements.append("You have included examples of handicaps.")
            
            if improvements:
                st.success("✅ Your revised answer shows improvement! Here’s what you did better:")
                for imp in improvements:
                    st.write(f"- {imp}")
            else:
                st.warning("⚠️ Try again! Ensure you include both the examples and their purposes.")
    
if __name__ == "__main__":
    main()
