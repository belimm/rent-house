function validate(){
    var userName = document.forms["formRegistration"]["userName"].value
    var password = document.forms["formRegistration"]["password"].value
    var passwordAgain = document.forms["formRegistration"]["passwordAgain"].value
    var name= document.forms["formRegistration"]["name"].value
    var gender = document.forms["formRegistration"]["gender"].value

    if(userName=="")
    {
        ("Username should be entered")
        return false
    }
        
    if(password=="")
    {
        alert("Password should be entered")
        return false
    }
        
    
    if(passwordAgain=="")
    {
        alert("Password should be reentered")
        return false
    }
    
    
    if(passwordAgain!=password)
    {
        alert("Password should be same")
        return false
    }
    
    
    if(name=="")
    {
        alert("Name should be entered")
        return false
    }
        
    
    if(gender=="")
    {
        alert("Gender should be entered")
        return false
    }
}