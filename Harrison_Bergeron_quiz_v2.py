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
        # Check if the answer is similar to the model answer
        similarity_feedback = compare_answers(response, model_answer)
        
        if similarity_feedback["match"]:
            st.success("✅ Great response! Here is some feedback on how you can improve your academic style and clarity:")
            st.write(similarity_feedback["improvement_suggestions"])
            
            st.subheader("Final Comparison with Model Answer")
            st.markdown(f"**Model Answer:** *{model_answer}*")
        else:
            st.warning("Your response could be improved. Let’s go step by step. There are two parts to this section, each should be written in clear, concise, academic style.")
            
            # Provide First Section of Text for Scaffolding
            st.subheader("Re-read This Section")
            st.markdown("*Nobody was smarter than anybody else. Nobody was better looking than anybody else. Nobody was stronger or quicker than anybody else.*")
            
            # Concept Checking for Understanding the Section
            intelligence_mcq = st.radio("What does this text say about intelligence?", 
                                       ["Everyone has different intelligence", "Everyone has different intelligence but the government tries to make it equal"],
                                       key="intelligence_mcq", index=None)
            if intelligence_mcq == "Everyone has different intelligence":
                st.error("❌ Incorrect. The text suggests that intelligence varies, but the government enforces equality.")
            elif intelligence_mcq:
                st.success("✅ Correct! The government uses devices to enforce equality.")
            
            beauty_mcq = st.radio("What does this text say about beauty?", 
                                 ["Everyone has different beauty", "Everyone has different beauty but the government tries to make it equal"],
                                 key="beauty_mcq", index=None)
            if beauty_mcq == "Everyone has different beauty":
                st.error("❌ Incorrect. The text shows that beauty varies, but the government enforces equality.")
            elif beauty_mcq:
                st.success("✅ Correct! The government enforces equality through handicaps like masks.")
            
            strength_mcq = st.radio("What does this text say about strength?", 
                                    ["Everyone has different strength", "Everyone has different strength but the government tries to make it equal"],
                                    key="strength_mcq", index=None)
            if strength_mcq == "Everyone has different strength":
                st.error("❌ Incorrect. The government prevents stronger individuals from using their abilities freely.")
            elif strength_mcq:
                st.success("✅ Correct! Strength varies, but the government enforces equality.")
            
            # How the Government Enforces Equality
            st.subheader("How does the government achieve this?")
            achievement_mcq = st.radio("How does the government make everyone equal?", 
                                      ["The government uses devices", "People are born the same", "People are trained to act the same"], 
                                      key="achievement_mcq", index=None)
            if achievement_mcq == "The government uses devices":
                st.success("✅ Correct! The government enforces equality through handicaps and restrictions.")
            elif achievement_mcq:
                st.error("❌ Incorrect. Think about how the story describes the enforcement of equality.")
            
            # Step 2: Summarizing the "Nobody was..." Section
            st.subheader("Summarize This Section")
            summary_response = st.text_area("Use this sentence starter to summarize: In this society, the government uses handicaps or devices to make sure that...", key="summary_nobody_was")
            
            if summary_response:
                if "same intelligence" in summary_response.lower() and "same beauty" in summary_response.lower() and "same strength" in summary_response.lower():
                    st.success("✅ Great job! Your summary includes the key points from the text.")
                else:
                    st.warning("Your summary is missing some key points. Make sure you mention intelligence, beauty, and strength.")
            
            st.subheader("Let's find the examples of the government's handicaps")

            # Now begin with the questions about George's father's device
            mcq1_key = "Q1_mcq1_unique"
            mcq1 = st.radio("What does George have to wear on his head?", 
                            ["A crown", "A mental radio", "A headband"], key=mcq1_key, index=None)
            
            if mcq1 == "A mental radio":
                st.success("✅ Correct! The mental radio disrupts his thoughts to prevent deep thinking.")
                
                # Concept Checking for Purpose
                mcq1_purpose_key = "Q1_mcq1_purpose"
                mcq1_purpose = st.radio("What is the purpose of the mental radio?", 
                            ["For George’s entertainment - he really likes music", 
                             "To prevent him from thinking too long", 
                             "To help him solve long problems, like using Google!"], 
                            key=mcq1_purpose_key, index=None)
                
                if mcq1_purpose == "To prevent him from thinking too long":
                    st.success("✅ Correct! The government limits intelligence by disrupting thoughts.")
                    
                    # Once Mental Radio Questions Are Done, Show Dancer Questions
                    mcq2_key = "Q1_mcq2"
                    mcq2 = st.radio("What do the dancers wear to make them equal?", 
                                    ["Heavy weights", "Light shoes", "Glasses"], key=mcq2_key, index=None)
                    
                    if mcq2 == "Heavy weights":
                        st.success("✅ Correct! The dancers wear weights to prevent them from moving gracefully.")
                        
                        # Concept Checking for Purpose
                        mcq2_purpose_key = "Q1_mcq2_purpose"
                        mcq2_purpose = st.radio("What is the purpose of the heavy weights?", 
                                    ["To help them move more freely", 
                                     "To make dancing harder so no one is better", 
                                     "To train them to be better athletes"], 
                                    key=mcq2_purpose_key, index=None)
                        
                        if mcq2_purpose == "To make dancing harder so no one is better":
                            st.success("✅ Correct! The weights ensure no one is naturally more skilled at dancing.")

                        # Open-ended question for examples
                        st.text_area("Give examples of different types of handicaps used. Start your answer with: For example,", key="examples_of_handicaps")

                        # Check if student included both examples and purposes
                        if st.session_state["examples_of_handicaps"]:
                            example_text = st.session_state["examples_of_handicaps"].lower()
                            has_example = any(word in example_text for word in ["radio", "weights", "mask"])
                            has_purpose = any(word in example_text for word in ["prevent", "limit", "hide", "disrupt"])
                            
                            if has_example and has_purpose:
                                st.success("✅ Well done! You've included both examples and their purposes.")
                            else:
                                st.warning("⚠️ Your answer is missing an important element. Make sure to include both an example and its purpose. For example: 'George's mental radio prevents him from thinking deeply.' Try revising your answer.")

                        # Ask students to rewrite their answer incorporating both elements
                        st.subheader("Rewrite Your Answer")
                        st.text_area("Now, rewrite your answer to the original question: 'What is the purpose of the handicaps used in the society of Harrison Bergeron? Give examples of different types of handicaps used.' Combine your previous two answers into a more complete response:", key="rewritten_answer")

                        # Compare with initial response
                        if st.session_state["rewritten_answer"]:
                            initial_answer = st.session_state["Q1_response"].lower()
                            rewritten_answer = st.session_state["rewritten_answer"].lower()
                            improvements = []

                            if len(rewritten_answer) > len(initial_answer):
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
            
            # Now begin with the questions about George's father's device
            mcq1_key = "Q1_mcq1_unique"
            mcq1 = st.radio("What does George have to wear on his head?", 
                            ["A crown", "A mental radio", "A headband"], key=mcq1_key, index=None)
    
if __name__ == "__main__":
    main()
