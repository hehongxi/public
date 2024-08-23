package com.example.demo.domain;

import lombok.Data;

@Data
public class UserEntity {
	
	
	// ここでユーザのモデルを作成してください	
    private Long id;

    private String name;
    private String password;
    private Integer sex;
    private Integer country;
    

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Integer getSex() {
        return sex;
    }

    public void setSex(Integer sex) {
        this.sex = sex;
    }
    
    public Integer getCountry() {
    	return country;
    }
    
    public void setCountry(Integer country) {
    	this.country = country;
    }
}


