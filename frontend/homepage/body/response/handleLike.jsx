import React, {useState} from "react";
import API from '../../baseURL/baseURL';
import heart from "../images/Heart.svg";
function Like(){
     const [count,setCount]=useState(0);
      const [liked, setLiked]=useState(false);
      const handleLike= async ()=>{
        try{
            const response=await API.get('/blogs/');
            await API.post(`/blogs/${response.data.id}/like/`);
            if(!liked){
        setCount(count+1);
      }
      else{
        setCount(count-1);
       }
       setLiked(!liked);
       }
       catch(err){
       console.log(`Error: ${err.message}`);
       }
    }
    return(
          <div className="likes">
           <div className="likeIcon">
             <button className="likeBtn" onClick={handleLike} ><img className="likestatus" src={heart} alt="heart" height={30} width={30} style={{ filter: liked ? "invert(23%) sepia(96%) saturate(7461%) hue-rotate(357deg)" : "none" }}/></button>
           </div>
            <div className="likecount">
              {count}
            </div>
          </div>);
 }
 export default Like;