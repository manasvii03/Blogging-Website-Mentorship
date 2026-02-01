import Response from '../response/response.jsx';
import calender from '../images/Calendar.svg';
import clock from '../images/Clock.svg';
import HandleSave from './handleSave.jsx'
import HandleStar from './handleStar.jsx'
import share from '../images/Send.svg';
function BlogCard({items}){
    return(
        <>
        {items.map((blog)=>(
        <div className="BlogCard" key={blog.id}>
         <div className="blogDetails">
            <div className="imageBlogLayout">
            <img className="imageBlog"src={blog.cover_image} alt="image"/></div>
            <div className="basicDetailsBlog">
                <h3 className="blogName">{blog.title}</h3>
                <p className="blogAuthorName"> By: <u>{blog.author_username}</u></p>
                <div className="blogCategory">{blog.category}</div>
            </div>
            
            <div className="timeRelatedandOthers">
             <div className="timeRelated">
                <div className="readtime"><img src={clock} alt="clock" width={25} height={25}/><p><b>Read Time: {blog.read_time} min</b></p></div>
                <div className="publishdate"><img src={calender} alt="calendar"width={25} height={25} /><p><b>Publish Date: {blog.
                  created_at}</b></p></div>
             </div>
             <div className="others">
                <HandleSave blogId={blog.id}/>
                <HandleStar blogId={blog.id}/>
                <div className="share"><button className="share"><img src={share} alt="share" width={30} height={30}/></button></div>
             </div>
            </div>
         </div>
        <Response blog={blog}/>
        </div>
        ))};
        </>
    );
}

export default BlogCard;