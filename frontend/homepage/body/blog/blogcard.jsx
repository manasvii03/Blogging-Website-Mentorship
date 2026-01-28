import Response from '../response/response.jsx';
import calender from '../images/Calendar.svg';
import clock from '../images/Clock.svg';
import save from '../images/save.svg';
import star from '../images/Star.svg';
import share from '../images/Send.svg';
import Blog from './blogdetails.jsx';
function BlogCard({items}){
    return(
        <>
        {items.map((Blog)=>(
        <div className="BlogCard">
         <div className="blogDetails">
            <div className="imageBlogLayout"><img className="imageBlog"src={Blog.image} alt="image"/></div>
            <div className="basicDetailsBlog">
                <h3 className="blogName">{Blog.blogName}</h3>
                <p className="blogSubheading">{Blog.subheading}</p>
                <p className="blogAuthorName">{Blog.authorName}</p>
            </div>
            <div className="timeRelatedandOthers">
             <div className="timeRelated">
                <div className="publishdate"><img src={calender} alt="calender" width={35} height={35}/><p><b>{Blog.publishDate}</b></p></div>
                <div className="readtime"><img src={clock} alt="clock" width={35} height={35}/><p><b>{Blog.readTime}</b></p></div>
             </div>
             <div className="others">
                <div className="save"><button className="save"><img src={save} alt="save" width={35} height={35}/></button></div>
                <div className="star"><button className="star"><img src={star} alt="star" width={35} height={35}/></button></div>
                <div className="share"><button className="share"><img src={share} alt="share" width={35} height={35}/></button></div>
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