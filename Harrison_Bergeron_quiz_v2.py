import streamlit as st

def main():
    st.title("Harrison Bergeron - Step-by-Step Quiz")
    
    # Provide text access
    with st.expander("Read this part of the story"):
        st.markdown("""
        **Harrison Bergeron** is a story about a world where everyone is forced to be equal. Here is a short part of the story:
        
        *Nobody was smarter than anybody else. Nobody was better looking than anybody else. Nobody was stronger or quicker than anybody else.*
        """)
    
    st.header("Let's Think About This Part")
    
    # Step 1: Concept Checking Question
    step1_key = "Q1_step1"
    if step1_key not in st.session_state:
        st.session_state[step1_key] = ""
    response1 = st.radio("What does this sentence mean?", ["Everyone was the same", "People were different", "I don't know"], key=step1_key)
    
    if response1 == "Everyone was the same":
        st.success("✅ That's right! The story says nobody was smarter, stronger, or better looking than anyone else.")
        
        # Step 2: Summarizing
        step2_key = "Q1_step2"
        if step2_key not in st.session_state:
            st.session_state[step2_key] = ""
        response2 = st.text_area("Now, explain this idea in **your own words** (1-2 sentences):", key=step2_key)
        
        if response2:
            st.success("Great! Now, let's go deeper.")
            
            # Step 3: Sentence Starter
            st.markdown("**Use this sentence starter to help you:**")
            st.markdown("*In this world, the government makes sure that...*")
            
            rewrite_key = "Q1_rewrite"
            if rewrite_key not in st.session_state:
                st.session_state[rewrite_key] = ""
            st.session_state[rewrite_key] = st.text_area("Finish the sentence in your own words:", st.session_state[rewrite_key])
            
            if st.session_state[rewrite_key]:
                st.success("You're doing great! Now, let's compare your answer with a model answer.")
                
                # Step 4: Model Answer
                model_answer = "In this world, the government makes sure that no one is smarter, stronger, or better looking than anyone else by giving people handicaps."
                st.markdown(f"**Model Answer:** *{model_answer}*")
                
                st.write("Now, let's see how close your answer is!")
                st.write(compare_answers(st.session_state[rewrite_key], model_answer))

def compare_answers(student_answer, model_answer):
    student_words = set(student_answer.lower().split())
    model_words = set(model_answer.lower().split())
    correct_words = student_words.intersection(model_words)
    missing_words = model_words - student_words
    
    return f"✅ Words you included: {', '.join(correct_words)}\n❌ Words you missed: {', '.join(missing_words)}"

if __name__ == "__main__":
    main()
