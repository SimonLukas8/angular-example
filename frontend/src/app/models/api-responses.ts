export interface UserAccount {
  username: string;
  token: string;
  id: number;
}

export interface ToDo {
  heading: string;
  content: string;
  tags: [number];
  imageUrl: string;
  date: null;
  user_id: null;
  id: null;
}

type TodoList = ToDo[];





