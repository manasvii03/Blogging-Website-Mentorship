import React, {useState} from 'react';
import comment from '../images/comment.svg';
import Like from './handleLike.jsx';
function Response({blog}){
    return(
 <div className="likeandcomment">
  <Like initialLike={blog.like_count} blogId={blog.id}/>
    <div className="comments">
       <button className="commentBtn">
        <img className="commentIconImg"src={comment} alt="comments" height={30} width={30}/>
       </button>
    </div>
 </div>
  
);
}
export default Response;