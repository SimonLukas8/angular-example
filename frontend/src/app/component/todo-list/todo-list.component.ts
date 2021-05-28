import { Component, OnInit } from '@angular/core';
import {AppModule} from "../../app.module";
import { TodoApiService } from "../../services/todo-api.service";
import { ToDo } from "../../models/api-responses";
import {CdkDragDrop, moveItemInArray, transferArrayItem} from '@angular/cdk/drag-drop';

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.scss']
})
export class TodoListComponent implements OnInit {


  todoo = [
    "Hallo",
    "Moin"
  ];

  drop(event: CdkDragDrop<ToDo[]>) {
    if (event.previousContainer === event.container) {
      moveItemInArray(event.container.data, event.previousIndex, event.currentIndex);
    } else {
      transferArrayItem(event.previousContainer.data,
        event.container.data,
        event.previousIndex,
        event.currentIndex);
    }
  }

  todo: ToDo[] | undefined; // todo is either an array or undefined if there are no todos

  constructor(
    private todoApiService: TodoApiService
  ) {

    this.todoApiService.getTodos().subscribe(answer => {
      this.todo = answer;
      console.log(this.todo);
    });

  }

  ngOnInit(): void {
  }

}
