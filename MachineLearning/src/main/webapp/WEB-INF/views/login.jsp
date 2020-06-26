<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@include file ="common/loginHeader.jsp" %>

<!-- HOME -->
<section class="home-section section-hero overlay bg-image" style="background-image: url('../resources/images/hero_1.jpg');" id="home-section">
	<div class="container">
		<div class="row align-items-center justify-content-center">
        	<div class="col-md-12">
				<div class="mb-5 text-center">
		            <h1 class="text-white font-weight-bold">출석 체크 로그인</h1>
					<p>수업 전 출석체크를 위해 로그인 해주시기 바랍니다.</p>
				</div>
				<form name="loginForm" method="post" action="loginForm" class="search-jobs-form" style="margin-left: 20%;">
					<div class="row mb-5">
						<div class="col-12 col-sm-6 col-md-6 col-lg-3 mb-4 mb-lg-0">
					    	<input type="text" name="userId" class="form-control form-control-lg" placeholder="professor ID">
					    </div>
					    <div class="col-12 col-sm-6 col-md-6 col-lg-3 mb-4 mb-lg-0">
					    	<input type="password" name="userPw" class="form-control form-control-lg" placeholder="professor PW">
					    </div>
						<div class="col-12 col-sm-6 col-md-6 col-lg-3 mb-4 mb-lg-0">
 							<button type="submit" onclick="login()" class="btn btn-primary btn-lg btn-block text-white btn-search"><span class="icon-search icon mr-2"></span>Login</button>
						</div>
					</div>
				</form>
			</div>
		</div>
	</div>
</section>

<script type="text/javascript">
	function login() {
	    var loginForm = document.loginForm;
	    var userId = loginForm.userId.value;
	    var userPw = loginForm.userPw.value;
	    
	    if(!userId || !userPw) {
	        alert("아이디와 비밀번호를 모두 입력해주세요.");
	        
	        return;
	    } else {
	        loginForm.submit();
	    }
	}
</script>
    
<%@include file ="common/footer.jsp" %>