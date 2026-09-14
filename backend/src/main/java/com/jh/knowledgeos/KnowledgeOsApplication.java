package com.jh.knowledgeos;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootApplication
@MapperScan("com.jh.knowledgeos.mapper")
public class KnowledgeOsApplication { public static void main(String[] args){SpringApplication.run(KnowledgeOsApplication.class,args);} }
