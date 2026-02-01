import LeftSidebar from "./leftSidebar/leftSidebar.jsx";
import RightSidebar from './rightSidebar/rightSidebar.jsx';
import Searchbar from './searchbar.jsx';
//import BlogCard from './blog/blogcard.jsx';
import BlogDetails from './blog/blogdetails.jsx';
import ForyouTrending from './foryoutrending.jsx';
function Body(){
    return(
        <>
        <div className="layout">
            <div className="sidebarLeft">
              <LeftSidebar/>
            </div>
            <div className="mainBody">
              <Searchbar/>
              <ForyouTrending/>
              <BlogDetails/>
            </div>
            <div className="sidebarRight">
              <RightSidebar/>
            </div>
     </div>
     </>
    );
}
export default Body;