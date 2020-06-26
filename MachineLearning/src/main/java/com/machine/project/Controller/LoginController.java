package com.machine.project.Controller;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Locale;

import javax.inject.Inject;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.machine.project.Dto.UserDto;
import com.machine.project.Service.UserService;

@Controller
public class LoginController {
	
	private static final Logger logger = LoggerFactory.getLogger(LoginController.class);
	
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String login(Locale locale, Model model) {
		
		return "login";
	}
	
	@RequestMapping(value = "/loginForm", method = RequestMethod.POST)
	public ModelAndView loginForm(@ModelAttribute UserDto userDto) throws Exception {
		ModelAndView mav;
		
		if(userDto.getUserId().equals("") || userDto.getUserPw().equals("")) {

			mav = new ModelAndView("login");
		} else {

			mav = new ModelAndView("myClass");
		}
		
		return mav;
	}
	
	@RequestMapping(value = "/insert", method = RequestMethod.POST)
	public String pythonFile() throws Exception {
		String result = "";
        
        Process process = Runtime.getRuntime().exec("python C:\\Users\\jeonjiwon\\Desktop\\Facial-Recognition\\Facial_Recognition_Part3.py");

        BufferedReader stb = new BufferedReader(new InputStreamReader(process.getInputStream()));
        BufferedReader ste = new BufferedReader(new InputStreamReader(process.getErrorStream()));


        while ((stb.readLine()) != null) {
            System.out.println("11111111111 :::::::::::: " + stb.readLine());
            result = "success";
        }
        while ((ste.readLine()) != null) {
            System.out.println("22222222222 :::::::::::: " + stb.readLine());
            System.out.println("22222222222 :::::::::::: " + stb.ready());
            System.out.println("22222222222 :::::::::::: " + stb.read());
            result = "fail";
        }
        return result;
	}
}
