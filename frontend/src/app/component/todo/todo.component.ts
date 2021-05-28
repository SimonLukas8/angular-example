import { Component, OnInit } from '@angular/core';
import { Input } from '@angular/core'; //used when an component gets data from a parent component


@Component({
  selector: 'app-todo',
  templateUrl: './todo.component.html',
  styleUrls: ['./todo.component.scss']
})
export class TodoComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
