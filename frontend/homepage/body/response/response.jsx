import heart from '../images/Heart.svg';
import React, {useState} from 'react';
import comment from '../images/comment.svg';
function Response(){
  const [count,setCount]=useState(0);
  //const [liked, setLiked]=useStyat
  const handleLike=()=>{
    setCount(count+1);
  }
  return(
 <div className="likeandcomment">
    <div className="likes">
     <div className="likeIcon">
       <button className="likeBtn" onClick={handleLike}><img className="likeIconImg"src={heart} alt="heart" height={35} width={35}/></button>
     </div>
      <div className="likecount">
       {count}
      </div>
    </div>
    <div className="comments">
       <button className="commentBtn">
        <img className="commentIconImg"src={comment} alt="comments" height={35} width={35}/>
       </button>
    </div>
 </div>
  
);
}
export default Response;