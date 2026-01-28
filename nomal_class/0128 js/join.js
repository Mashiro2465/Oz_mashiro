const form = document.getElementById("form")

form.addEventListener("submit", function(e){
  e.preventDefault();

  let userId = e.target.id.value
  let userPw1 = e.target.pw1.value
  let userPw2 = e.target.pw2.value
  let userName = e.target.name.value
  let userPhone = e.target.phone.value
  let userPosition = e.target.position.value
  let userGender = e.target.gender.value
  let userEmail = e.target.email.value
  let userIntro = e.target.intro.value

  console.log(
    `
    아이디 : ${userId} 
    비밀번호 : ${userPw1}, 
    비밀번호 확인 : ${userPw2} 
    이름 : ${userName} 
    전화번호 : ${userPhone} 
    희망 직무 : ${userPosition} 
    성별 : ${userGender} 
    이메일 : ${userEmail} 
    자기소개 : ${userIntro} 
    `
  )

  if(userId.length < 6){
    alert("아이디가 너무 짧습니다. 6자 이상 입력해주세요.")
    return;
  }

  if(userPw1 !== userPw2){
    alert("비밀번호가 일치하지 않습니다.")
    return;
  }

  document.body.innerHTML = ""
  document.write(`<p>${userId}님 환영합니다</p>`)
})