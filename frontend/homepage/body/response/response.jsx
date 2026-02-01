import React, {useState} from 'react';
import comment from '../images/comment.svg';
import Like from './handleLike.jsx';
function Response(){
    return(
 <div className="likeandcomment">
  <Like/>
    <div className="comments">
       <button className="commentBtn">
        <img className="commentIconImg"src={comment} alt="comments" height={30} width={30}/>
       </button>
    </div>
 </div>
  
);
}
export default Response;