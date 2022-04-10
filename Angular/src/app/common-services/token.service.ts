import { HttpInterceptor } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TokenService implements HttpInterceptor {

  constructor() { }
  intercept ( req : any , next : any ){
    if (req.headers.get("skip")){
      return next.handle( req );
    }else{
      const strUserData : string = localStorage.getItem('userData') || ''
      const userData : any = JSON.parse ( strUserData )
      console.log()
      const tokenizedReq = req.clone({
        setHeaders: {
          Authorization : `Bearer xx.yy.zz`,
          'x-access-token' :  userData['token'],
        }
      });
      return next.handle( tokenizedReq );
    }

  }
}
