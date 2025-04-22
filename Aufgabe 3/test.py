from my_classes import Subject

if __name__ == "__main__":
    subj = Subject(
        name="Simon",
        gender="male",
        birthdate="2003-05-15",
        weight=70,
        height=175,
        resting_hr=60,
        email="simon@alt.de"
    )
    
    print("==> Erstelle Person …")
    subj.put()  

    subj.email = "simon@neu.de"
    print("==> Aktualisiere E-Mail …")
    subj.update_email() 





