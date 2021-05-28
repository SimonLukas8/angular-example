import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import { UserAccount } from "../models/api-responses";
import { ToDo } from "../models/api-responses";

@Injectable({
  providedIn: 'root'
})
export class TodoApiService {

  constructor(
    private http : HttpClient //instanz, typ
  ) {

  }

  getAccount(): Observable<UserAccount> {
    return this.http.get<UserAccount>("http://localhost:8080/account");//wenn man Klassenvariable haben möchte dann
  }

  getTodos(): Observable<ToDo[]> {
    return this.http.get<ToDo[]>("http://localhost:8080/todo");
  }

  //postTodos(): Observable<newToDo> {
    //return this.http.post<newToDo>("http://localhost:8080/todo", );
  //}

}


