import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { LoginModel, QueryModel, UserModel } from '../login/login';
import { apiUrl } from '../models/_config';
import { catchError, throwError } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class UserService {
  loginUrl = `${apiUrl}/login`;
  showUsersUrl = `${apiUrl}/showusers`;
  addUserUrl = `${apiUrl}/addusers`
  constructor( private http : HttpClient) { }
  errorHandler(error : HttpErrorResponse){
    return throwError(error)
  }
  loggedIn() : boolean{
    return !!localStorage.getItem('userData');
  }

  showUsers(queryModel ? : QueryModel){
    return this.http.post<any>(this.showUsersUrl, queryModel)
      .pipe(catchError(this.errorHandler))
  }

  addUser(userModel : UserModel) : Observable <any>{
    return this.http.post<any>(this.addUserUrl, userModel)

  }



}
