import homeIcon from '../images/Home.svg';
import bookmarkIcon from '../images/Bookmark.svg';
import barchartIcon from '../images/Barchart.svg';
import personIcon from '../images/person.svg';
import group2Icon from '../images/Group2.svg';
function LeftSidebar(){
    return(
    <div className="sidebarLeftIcons">
                   <div className="homeIcon">
                    <button className="homeBtn">
                    <img src={homeIcon} alt="home" width={45} height={45}/>
                    </button>
                   </div>
                   <div className="bookmarkIcon">
                    <button className="bookmarkBtn">
                    <img src={bookmarkIcon} alt="bookmark" width={45} height={45}/>
                    </button>
                   </div>
                   <div className="group2">
                    <button className="group2Btn">
                    <img src={group2Icon} alt="group2" width={40} height={40}/>
                    </button>
                   </div>
                   <div className="barchartIcon">
                    <button className="barchartBtn">
                    <img src={barchartIcon} alt="barchart" width={45} height={45}/>
                    </button>
                   </div>
                   <div className="personBodyIcon">
                    <button className="personBodyBtn">
                    <img src={personIcon} alt="person" width={35} height={35}/>
                    </button>
                   </div>                
                </div>
    );
}
export default LeftSidebar;