package com.machine.project.Controller;

import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.machine.project.Dto.UserDto;

@Controller
public class LoginController {
	
	private static final Logger logger = LoggerFactory.getLogger(LoginController.class);
	
	@RequestMapping(value = "/", method = {RequestMethod.GET,RequestMethod.POST})
	public String login(Locale locale, Model model) {
		
		return "login";
	}
	
	@RequestMapping(value = "/loginForm", method = RequestMethod.POST)
	public String loginForm() throws Exception {
		
		System.out.println("userDto :::::::::::::: " );
		
		return "myClass";
	}
}
