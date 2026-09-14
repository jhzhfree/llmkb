package com.jh.knowledgeos.controller;
import com.jh.knowledgeos.common.ApiResponse;import com.jh.knowledgeos.service.KnowledgeService;import org.springframework.web.bind.annotation.*;import java.util.*;
@RestController @RequestMapping("/api/knowledge") @CrossOrigin public class KnowledgeController{private final KnowledgeService s;public KnowledgeController(KnowledgeService s){this.s=s;}
@PostMapping("/extract") public ApiResponse<Object> extract(@RequestBody Map<String,Object> r){return ApiResponse.ok(s.extract(r));}
@PostMapping("/adjudicate") public ApiResponse<Object> adjudicate(@RequestBody Map<String,Object> r){return ApiResponse.ok(s.adjudicate(r));}
@PostMapping("/query") public ApiResponse<Object> query(@RequestBody Map<String,Object> r)throws Exception{return ApiResponse.ok(s.query(r));}
@GetMapping("/cards/{kb}") public ApiResponse<Object> cards(@PathVariable Long kb){return ApiResponse.ok(s.cards(kb));}
@GetMapping("/claims/{kb}") public ApiResponse<Object> claims(@PathVariable Long kb){return ApiResponse.ok(s.claims(kb));}
@GetMapping("/trace/{qid}") public ApiResponse<Object> trace(@PathVariable String qid){return ApiResponse.ok(s.trace(qid));}}
