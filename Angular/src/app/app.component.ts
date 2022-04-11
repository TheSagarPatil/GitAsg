import { Component } from '@angular/core';
import { timer } from 'rxjs';
import { UserService } from './common-services/user.service';
import { RolesComponent } from './roles/roles.component';
import { UsersComponent } from './users/users.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app1';
  constructor(
    private userService : UserService,
  ){}
  getRefreshToken(){
    this.userService.getRefreshToken().subscribe(
      data => {
        if (data){
          localStorage.setItem('userData', JSON.stringify(data))
          console.log ( 'success token refreshed', data );
        }
      }
    )
  }
  callGetRefreshToken(){
    setInterval(()=>{
      this.getRefreshToken();
    }, 4000);
  }
}
