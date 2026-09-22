-- Keep the generated bibliography readable without HTML layout wrappers.
-- Citations are numeric; PDF output retains the linked CSL formatting.
function Div(element)
  return element.content
end

function Span(element)
  return element.content
end

-- Display equations must be separate blocks in Markdown renderers.
function Para(element)
  local blocks = pandoc.List()
  local inlines = pandoc.List()
  local found = false
  for _, item in ipairs(element.content) do
    if item.t == "Math" and item.mathtype == "DisplayMath" then
      found = true
      if #inlines > 0 then
        blocks:insert(pandoc.Para(inlines))
        inlines = pandoc.List()
      end
      blocks:insert(pandoc.RawBlock("markdown", "$$\n" .. item.text .. "\n$$"))
    else
      inlines:insert(item)
    end
  end
  if not found then return nil end
  if #inlines > 0 then blocks:insert(pandoc.Para(inlines)) end
  return blocks
end
