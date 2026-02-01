import Response from '../response/response.jsx';
import calender from '../images/Calendar.svg';
import clock from '../images/Clock.svg';
import save from '../images/save.svg';
import star from '../images/Star.svg';
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
            </div>
            <div className="timeRelatedandOthers">
             <div className="timeRelated">
                <div className="readtime"><img src={clock} alt="clock" width={25} height={25}/><p><b>Read Time: {blog.read_time} min</b></p></div>
                <div className="publishdate"><img src={calender} alt="calendar"width={25} height={25} /><p><b>Publish Date:</b></p></div>
             </div>
             <div className="others">
                <div className="save"><button className="save"><img src={save} alt="save" width={30} height={30}/></button></div>
                <div className="star"><button className="star"><img src={star} alt="star" width={30} height={30}/></button></div>
                <div className="share"><button className="share"><img src={share} alt="share" width={30} height={30}/></button></div>
             </div>
            </div>
         </div>
        <Response/>
        </div>
        ))};
        </>
    );
}

export default BlogCard;