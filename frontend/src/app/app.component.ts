import {Component} from '@angular/core';
import {TodoApiService} from "./services/todo-api.service";
import {ToDo, UserAccount} from "./models/api-responses";


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'todo-list';
  user: UserAccount | undefined; //oder falls es den User Account nicht gibt
  todo: ToDo[] | undefined;

  constructor(
    private todoApiService: TodoApiService
  ) {
    this.todoApiService.getAccount().subscribe(answer => {
      this.user = answer;
    });
    this.todoApiService.getTodos().subscribe(answer => {
      this.todo = answer;
      console.log(answer);
    });
  }
}
