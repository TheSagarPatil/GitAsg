import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { interval } from 'rxjs/internal/observable/interval';
import { take } from 'rxjs/internal/operators/take';
import { LoginService } from '../common-services/login.service';
import { UserService } from '../common-services/user.service';
import { LoginModel } from './login';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  //roles : string[] = ['Admin', 'Read', 'Write'];
  loginModel = new LoginModel( '', '' )
  errorMessage : string = "";
  constructor(
    private userService : UserService,
    private router : Router,
    private loginService : LoginService,
    ) { }

  ngOnInit(): void {
    localStorage.setItem('userData', '');
  }
  loginClicked($event : any){
    console.log($event);
  }
  onSubmit(){
    console.log(this.loginModel)
    this.loginService.login(this.loginModel).subscribe(
      data => {
        this.successHandler(data);
      },
      errr => {
        this.errorMessage = 'fail'
        console.log ( 'success', errr );
      }
    )
  }
  successHandler(data : any){
    this.errorMessage = 'success'
    localStorage.setItem('userData', JSON.stringify(data))
    console.log ( 'success', data );
    interval(2000).pipe(take(1), ).subscribe(value =>{
      this.errorMessage = '';
      this.router.navigate(['/users']);
    });
  }

}
