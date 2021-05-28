import { Component, OnInit } from '@angular/core';
import {TodoApiService} from "../../services/todo-api.service";
import { ToDo } from "../../models/api-responses";

@Component({
  selector: 'app-todo-new-input',
  templateUrl: './todo-new-input.component.html',
  styleUrls: ['./todo-new-input.component.scss']
})
export class TodoNewInputComponent implements OnInit {

/*newToDo : ToDo[] | undefined;

  constructor(
    private todoApiService: TodoApiService
  ) {

    this.todoApiService.postTodos().subscribe(request => {
      this.newToDo = request;
      console.log(this.newToDo);
    });

  } */

  ngOnInit(): void {
  }

}
