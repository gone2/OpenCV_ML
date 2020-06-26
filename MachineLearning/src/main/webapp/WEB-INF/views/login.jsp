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
            <div style="margin-left: 20%;">
	            <form method="post" class="search-jobs-form">
	              <div class="row mb-5">
	                <div class="col-12 col-sm-6 col-md-6 col-lg-3 mb-4 mb-lg-0">
	                  <input type="text" class="form-control form-control-lg" placeholder="professor ID">
	                </div>
	                <div class="col-12 col-sm-6 col-md-6 col-lg-3 mb-4 mb-lg-0">
	                  <input type="password" class="form-control form-control-lg" placeholder="professor PW">
	                </div>
	                <div class="col-12 col-sm-6 col-md-6 col-lg-3 mb-4 mb-lg-0">
	                  <button type="submit" class="btn btn-primary btn-lg btn-block text-white btn-search"><span class="icon-search icon mr-2"></span>Login</button>
	                </div>
	              </div>
	            </form>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <script>
    	
    </script>
    
<%@include file ="common/footer.jsp" %>