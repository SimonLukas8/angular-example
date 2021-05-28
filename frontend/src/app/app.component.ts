import {Component} from '@angular/core'; //Implements Angular''s core functionality, low-level services, and utilities.
// Defines the class infrastructure for components, view hierarchies, change detection, rendering, and event handling
import {TodoApiService} from "./services/todo-api.service";
import {ToDo, UserAccount} from "./models/api-responses";


@Component({ //Decorator specifies meta data for program structures like classes
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {  // export means that the class can be used by other files
  title = 'todo-list'; //name of the html element that represents the component
  user: UserAccount | undefined; //oder falls es den User Account nicht gibt


  constructor(
    private todoApiService: TodoApiService
  ) {
    this.todoApiService.getAccount().subscribe(answer => {
      this.user = answer;
    });

  }
}

