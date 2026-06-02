def common_skills(skillset1,skillset2):
    if not skillset1 or not skillset2:
        print("Invalid Skillset")
        return
    common=skillset1 & skillset2
    print(f"Common Skills are :{common}")
skills1={"Python","SQL","Java"}
skills2={"Python", "C++", "SQL"}
common_skills(skills1,skills2)