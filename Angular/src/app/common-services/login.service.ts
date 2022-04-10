import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { LoginModel, QueryModel, UserModel } from '../login/login';
import { apiUrl } from '../models/_config';
import { catchError, throwError } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class LoginService {
  loginUrl = `${apiUrl}/login`;

  constructor( private http : HttpClient) { }
  errorHandler(error : HttpErrorResponse){
    return throwError(error)
  }

  login(loginModel : LoginModel) : Observable<any>{
    return this.http.post<any>(this.loginUrl, loginModel, {headers:{skip:"true"} })
      .pipe(catchError(this.errorHandler))
  }
}
