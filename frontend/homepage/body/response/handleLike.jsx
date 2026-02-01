import React, {useState} from "react";
import API from '../../baseURL/baseURL';
function Like({initialLike,blogId}){
     const [count,setCount]=useState(initialLike);
      const [liked, setLiked]=useState(false);
      const handleLike= async ()=>{
        const user_token = localStorage.getItem('token');
        try{
             if(!liked){ 
              setCount(count+1);
             }
             else{
              setCount(count-1);
             }
             setLiked(!liked);
            await API.post(`/blogs/${blogId}/like/`, {}, {
            headers: {
                    'Authorization': `Token ${user_token}`, 
                    'Content-Type': 'application/json'}});
            
          }
       catch(err){
       console.log(`Error: ${err.message}`);
       }
    }
    return(
          <div className="likes">
           <div className="likeIcon">
             <button className="likeBtn" onClick={handleLike} ><svg className={liked ? "liked" : "notliked"}  width="30"  height="30" viewBox="0 0 46 41" fill="none" >
              <path d="M40.5826 5.22365C39.5611 4.20166 38.3482 3.39094 37.0133 2.83782C35.6784 2.28469 34.2476 2 32.8026 2C31.3576 2 29.9268 2.28469 28.5919 2.83782C27.257 3.39094 26.0441 4.20166 25.0226 5.22365L22.9026 7.34365L20.7826 5.22365C18.7192 3.16027 15.9206 2.00107 13.0026 2.00107C10.0845 2.00107 7.28597 3.16027 5.22258 5.22365C3.1592 7.28704 2 10.0856 2 13.0037C2 15.9217 3.1592 18.7203 5.22258 20.7837L22.9026 38.4636L40.5826 20.7837C41.6046 19.7621 42.4153 18.5493 42.9684 17.2144C43.5215 15.8794 43.8062 14.4486 43.8062 13.0037C43.8062 11.5587 43.5215 10.1279 42.9684 8.79294C42.4153 7.45802 41.6046 6.24516 40.5826 5.22365Z"/></svg></button>
           </div>
            <div className="likecount">
              {count}
            </div>
          </div>);
 }
 export default Like;