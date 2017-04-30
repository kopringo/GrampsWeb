import { Injectable }     from '@angular/core';
import { Http, Response } from '@angular/http';
import { Person }           from '../models/person';
import { Observable }     from 'rxjs/Observable';

@Injectable()
export class TreeService {
  private heroesUrl = 'api/v1/';  // URL to web API
  constructor (private http: Http) {}
  
  public getList(){
	  //var dupa = Person[];
	  return [];
  }
  
  private extractData(res: Response) {
    let body = res.json();
    return body.data || { };
  }
  private handleError (error: Response | any) {
    // In a real world app, we might use a remote logging infrastructure
    let errMsg: string;
    if (error instanceof Response) {
      const body = error.json() || '';
      const err = body.error || JSON.stringify(body);
      errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
    } else {
      errMsg = error.message ? error.message : error.toString();
    }
    console.error(errMsg);
    return Observable.throw(errMsg);
  }
}