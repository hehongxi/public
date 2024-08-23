package com.example.demo.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.DataClassRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.example.demo.domain.UserEntity;

//定义了一个控制器
@Controller//这是MVC里的控制器
@RequestMapping()//处理任何页面的请求
public class DemoController {
	
	@Autowired//利用注解自动注入
    private JdbcTemplate jdbcTemplate;
	
	@GetMapping("/index")
    private String index(){
		return "index.html";//去到index画面
    }
	
	@GetMapping("/add")
	private String add(){
		return "add.html";//去add画面
    }
	
	
	@GetMapping("/show")
	public String show(Model model) {
		String sql="SELECT * FROM user_info";//查询数据库里面所有的用户信息
		List<UserEntity> list = jdbcTemplate.query(sql, new DataClassRowMapper<>(UserEntity.class));
        model.addAttribute("userList", list);//查询结果全部给到userlist模型，方便html取用
        return "show.html";//回到show画面
	}
	
	@ResponseBody
	@PostMapping("/regist")
	
	public String postMethodName( @ModelAttribute UserEntity user) {
		String sql="INSERT INTO user_info(name,password,sex,country) value(?,?,?,?);";
		jdbcTemplate.update(sql, user.getName(), user.getPassword(), user.getSex(), user.getCountry());//把新的用户数据插入数据库
		//return "登録完了<br><a href=\"index\">メニューに戻る</a>";
	    return "<html><body>"
	    		
        + "<script type=\"text/javascript\">"
        + "alert('登录完成');"
        + "window.location.href = 'index';" // 跳转到主页
        + "</script>"
        
        + "</body></html>";
	}

}
