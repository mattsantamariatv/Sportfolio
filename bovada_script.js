//Puppeteer is a Node library which provides a high-level API to control Chrome or Chromium over the DevTools Protocol
//The fs module of Node.js provides useful functions to interact with the file system.

const puppeteer = require('puppeteer');
const fs = require('fs');

//Async functions enable us to write promise based code as if it were synchronous, but without blocking the execution thread.
//The await expression causes async function execution to pause until a Promise is settled (that is, fulfilled or rejected)

async function run() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  const TEAM_NAME = '.coupon-content.more-info';

//Try and catch - The try statement allows you to define a block of code to be tested for errors while it is being executed.
  
  try  {
    await page.goto('https://www.bovada.lv/sports/baseball/mlb?overlay=false');
    await page.screenshot({ path: 'screenshots/latest.png' });
  } catch(err) {
    console.log({err})
  }
  
//The console event is emitted when javascript within the page calls a console API message (like console.log).

//The Document method querySelectorAll() returns a static (not live) NodeList representing 
//a list of the document's elements that match the specified group of selectors

//page(). An array of all pages inside the Browser.
  
//The querySelectorAll() method returns all elements in the document that matches a specified CSS selector(s), as a static NodeList object.
//The NodeList object represents a collection of nodes. The nodes can be accessed by index numbers. The index starts at 0.  
  
  page.on('console' , msg => console.log(msg));
  const teamNameHandle = await page.evaluate((selector) => {
      return [...document.querySelectorAll(selector)].map((node, index) => {
      return {
        match : index,
        teamOne : {
          name : node.querySelectorAll('.name')[0].innerText,
          runline : node.querySelectorAll('.bet-price')[0].innerText.replace(/[()]/gi, ''),
          win : node.querySelectorAll('.bet-price')[2].innerText.replace(/[()]/gi, ''),
          total : node.querySelectorAll('.bet-price')[4].innerText.replace(/[()]/gi, '')
        },
        teamTwo : {
          name : node.querySelectorAll('.name')[1].innerText,
          runline : node.querySelectorAll('.bet-price')[1].innerText.replace(/[()]/gi, ''),
          win : node.querySelectorAll('.bet-price')[3].innerText.replace(/[()]/gi, ''),
          total : node.querySelectorAll('.bet-price')[5].innerText.replace(/[()]/gi, '')
        }
      }
    });
  }, TEAM_NAME);

  //The JSON.stringify() method converts a JavaScript object or value to a JSON string.
  
  const jsonContent = JSON.stringify(teamNameHandle);

  fs.writeFile("output/result.json", jsonContent, 'utf8', function (err) {
    if (err) {
        console.log("An error occured while writing result to File.");
        return console.log(err);
    }
    console.log('result written to output/result.json');
  });

  await browser.close();
}

run();
